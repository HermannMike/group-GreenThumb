import { useState } from "react";
import ReminderForm from "./ReminderForm";
import ReminderItem from "./ReminderItem";

const ReminderList = () => {
  const [reminders, setReminders] = useState([]);

  const addReminder = (reminder) => setReminders([...reminders, reminder]);
  const deleteReminder = (id) => setReminders(reminders.filter((r) => r.id !== id));

  return (
    <div>
      <ReminderForm onAdd={addReminder} />
      <ul>
        {reminders.map((reminder) => (
          <ReminderItem key={reminder.id} reminder={reminder} onDelete={deleteReminder} />
        ))}
      </ul>
    </div>
  );
};

export default ReminderList;