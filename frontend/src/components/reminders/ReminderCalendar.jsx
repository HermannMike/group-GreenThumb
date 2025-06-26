import { useState } from "react";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";

const ReminderCalendar = ({ reminders }) => {
  const [selectedDate, setSelectedDate] = useState(new Date());

  const getRemindersForDate = (date) => {
    const d = date.toISOString().split("T")[0];
    return reminders.filter((r) => r.date === d);
  };

  return (
    <div>
      <Calendar onChange={setSelectedDate} value={selectedDate} />
      <h3 className="mt-4">Reminders for {selectedDate.toDateString()}:</h3>
      <ul>
        {getRemindersForDate(selectedDate).map((r) => (
          <li key={r.id}>{r.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default ReminderCalendar;