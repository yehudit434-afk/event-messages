import traceback
from events_reader import (
    load_recurring_events, load_temporary_events,
    mark_as_sent, is_already_sent, log_sent,
)
from hebrew_date import parse_hebrew_date, get_recent_hebrew_dates
from message_builder import build_message
from email_sender import send_email, send_error_email


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
            print(f"✅ נשלח: {subject}")
            found = True

    if not found:
        print("אין אירועים קבועים לשליחה.")


def process_temporary_events():
    """Sends greetings for unsent temporary events."""
    events = load_temporary_events()

    if not events:
        print("אין אירועים זמניים לשליחה.")

    for event in events:
        subject, body = build_message(event)
        send_email(subject=subject, body=body)
        mark_as_sent(event)
        print(f"✅ נשלח: {subject}")


def main():
    print("--- אירועים קבועים ---")
    process_recurring_events()
    print("\n--- אירועים זמניים ---")
    process_temporary_events()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        error = traceback.format_exc()
        print(f"❌ שגיאה:\n{error}")
        try:
            send_error_email(error)
            print("📧 מייל שגיאה נשלח.")
        except Exception:
            print("❌ לא הצלחתי לשלוח מייל שגיאה.")
