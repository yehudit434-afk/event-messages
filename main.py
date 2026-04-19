import traceback
from events_reader import (
    load_recurring_events, load_temporary_events,
    mark_as_sent, is_already_sent, log_sent,
)
from hebrew_date import parse_hebrew_date, get_recent_hebrew_dates
from message_builder import build_message
from email_sender import send_email, send_error_email
from constants import (
    MSG_SENT, MSG_NO_RECURRING, MSG_NO_TEMPORARY,
    MSG_RECURRING_HEADER, MSG_TEMPORARY_HEADER,
    MSG_ERROR, MSG_ERROR_EMAIL_SENT, MSG_ERROR_EMAIL_FAILED,
)


def process_recurring_events():
    """Sends greetings for recurring events from the last 7 days that weren't sent yet."""
    recent_dates = get_recent_hebrew_dates()
    events = load_recurring_events()

    found = False
    for event in events:
        event_date = parse_hebrew_date(event.date)
        if event_date in recent_dates and not is_already_sent(event, event.date):
            subject, body = build_message(event)
            send_email(subject=subject, body=body)
            log_sent(event, event.date)
            print(MSG_SENT.format(subject=subject))
            found = True

    if not found:
        print(MSG_NO_RECURRING)


def process_temporary_events():
    """Sends greetings for unsent temporary events."""
    events = load_temporary_events()

    if not events:
        print(MSG_NO_TEMPORARY)

    for event in events:
        subject, body = build_message(event)
        send_email(subject=subject, body=body)
        mark_as_sent(event)
        print(MSG_SENT.format(subject=subject))


def main():
    print(MSG_RECURRING_HEADER)
    process_recurring_events()
    print(f"\n{MSG_TEMPORARY_HEADER}")
    process_temporary_events()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        error = traceback.format_exc()
        print(MSG_ERROR.format(error=error))
        try:
            send_error_email(error)
            print(MSG_ERROR_EMAIL_SENT)
        except Exception:
            print(MSG_ERROR_EMAIL_FAILED)
