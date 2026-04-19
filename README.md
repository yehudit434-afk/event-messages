# 🎉 FamilyMessages

Automated script for sending family greeting emails to a Google Group, based on Hebrew calendar dates.

## 📋 Description

The system sends styled HTML greeting messages to a Google Group based on family events.
Events and templates are managed through an Excel file — no code changes needed.

### Supported Event Types

**Recurring events** (Hebrew date, yearly):
- 🎂 Birthday (male / female)
- 💍 Wedding anniversary (couple)

**One-time events:**
- 👶 Birth of son / daughter / twins
- 💍 Engagement
- 🌟 Pidyon HaBen
- 🎉 Welcome
- Any custom event added to the templates sheet

## 📁 Project Structure

```
Messages/
├── main.py              # Entry point - runs everything
├── config.py            # Path settings (supports EXE mode)
├── events_reader.py     # Reads events from Excel
├── message_builder.py   # Builds styled HTML messages
├── email_sender.py      # Sends email via Gmail SMTP
├── hebrew_date.py       # Hebrew date conversion
├── Events.xlsx          # Events and templates file
├── .env                 # Credentials (do not share!)
└── README.md
```

## ⚙️ Setup

### Prerequisites
- Python 3.10+
- Gmail account with 2-Step Verification enabled

### Install packages
```bash
py -m pip install -r requirements.txt
```

### Create Gmail App Password
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Security → 2-Step Verification (make sure it's enabled)
3. Search for "App passwords"
4. Create a new password and copy it

### Prepare Excel file
Rename `Events.example.xlsx` to `Events.xlsx` and fill in your data.

### Configure `.env`
```
SENDER_EMAIL=your-email@gmail.com
APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
GROUP_EMAIL=your-group@googlegroups.com
```

## 📊 Excel File Structure

The file `Events.xlsx` contains 4 sheets:

### Sheet "אירועים" (Events) - Recurring events
| תאריך (Date) | שם (Name) | מין (Gender) | אירוע (Event) |
|--------------|-----------|-------------|---------------|
| כ"ה ניסן | יעל | נקבה | יום הולדת |
| א' תשרי | דני ושרה | זוג | יום נישואין |

**Hebrew date format:**
- Single letter: `א' תשרי`
- Two letters: `י"ב אייר`, `כ"ה כסלו`

### Sheet "אירועים זמניים" (Temporary Events) - One-time events
| תאריך (Date) | שם (Name) | שם התינוק (Baby Name) | מין (Gender) | אירוע (Event) | נשלח (Sent) |
|--------------|-----------|----------------------|-------------|---------------|------------|
| 25/05/2025 | דני ושרה | דניאל | זוג | הולדת בן | |

- "נשלח" (Sent) column is automatically updated to "כן" after sending
- Empty fields are allowed (e.g. "ברוך הבא" without a name)

### Sheet "תבניות" (Templates) - Message templates
| אירוע (Event) | מין (Gender) | נושא (Subject) | גוף (Body) | צבע רקע (BG Color) |
|---------------|-------------|----------------|------------|-------------------|
| יום הולדת | נקבה | 🎂✨ מזל טוב ל{name}... | הרבה אושר...{br}ימים טובים... | #fff0f5 |

**Available variables:**
- `{name}` - Name from Excel
- `{baby_name}` - Baby name
- `{br}` - Line break

**Recommended background colors:**
- `#fff0f5` - Light pink (female)
- `#f0f8ff` - Light blue (male)
- `#fdf5e6` - Cream (couple)
- `#e8f5e9` - Light green (welcome)
- `#fffff0` - Light yellow (pidyon)

### Sheet "לוג שליחות" (Send Log) - Sending history
| תאריך עברי (Hebrew Date) | שם (Name) | אירוע (Event) | תאריך שליחה (Send Date) |
|--------------------------|-----------|---------------|------------------------|

Filled automatically. Prevents duplicate sending of recurring events.

## 🚀 Usage

```bash
py main.py
```

### Example output
```
--- אירועים קבועים ---
✅ נשלח: 🎂✨ מזל טוב ליעל ליום הולדתה! ✨🎂

--- אירועים זמניים ---
✅ נשלח: 👶✨ מזל טוב לדני ושרה להולדת הבן דניאל המתוק! ✨👶
```

## 🖥️ Running as EXE (without Python)

### Build EXE
```bash
py -m pip install pyinstaller
py -m PyInstaller --onefile --name EventMessages main.py
```

### Transfer to another computer
Copy 3 files to the same folder:
1. `dist/FamilyMessages.exe`
2. `Events.xlsx`
3. `.env`

## ⏰ Automatic Scheduling - Task Scheduler

1. Open Task Scheduler (`Win+R` → `taskschd.msc`)
2. Create Task:
   - **General:** Check "Run whether user is logged on or not"
   - **Triggers:** Weekly → Sunday to Friday, 08:00
   - **Actions:** Start a program → path to EXE, "Start in" → its folder
   - **Settings:** Check "Run task as soon as possible after a scheduled start is missed"

## 🔒 Security

- Credentials are stored in `.env`, not in code
- If sharing the project, **do not share `.env`**
- Recommended to add `.env` to `.gitignore`

## ❌ Error Handling

If an error occurs during execution, the system:
1. Prints the error to the terminal
2. Sends an email with error details to `SENDER_EMAIL`

## 💡 Adding a New Event Type

Want to add a new event type (e.g. "Bar Mitzvah")?
1. Add a row in the **"תבניות"** (Templates) sheet with the desired text
2. Add the event in the **"אירועים"** (Events) or **"אירועים זמניים"** (Temporary Events) sheet
3. That's it! No code changes needed 🎉
