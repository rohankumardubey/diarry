import settings
import models
import textwrap


def fetch_all_entries_sorted_by_date():
    """
    Returns all the Diary Entries ordered by date descending (oldest first)
    """
    return settings.session.query(models.DiaryEntry)\
        .order_by(models.DiaryEntry.creation_date.asc(), models.DiaryEntry.creation_time.asc())\
        .all()


def format_diary_entry(entry: models.DiaryEntry) -> str:
    """
    Formats a single Diary Entry to the wanted format to be outputted in the .txt file
    """
    entry_id = entry.id
    title = entry.title
    body = entry.body
    date = entry.creation_date.strftime("%d %B %Y")
    time = entry.creation_time.strftime("%H:%M")

    formatted_entry = f"""\t\t\t\t\t\t\t{title}
#{entry_id} - {date} {time}

{body}
    """
    return formatted_entry


def write_entries_to_file():
    """
    Writes all the diary entries to the file
    :return:
    """
    with open('diary.txt', 'w') as diary_file:
        for diary_entry in fetch_all_entries_sorted_by_date():
            diary_file.write(format_diary_entry(diary_entry))
            diary_file.write('\n' + '-' * 100 + '\n')
