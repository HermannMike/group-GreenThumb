const ReminderItem = ({ reminder, onDelete }) => (
  <li>
    {reminder.text} - {reminder.date}
    <button onClick={() => onDelete(reminder.id)}>Delete</button>
  </li>
);

export default ReminderItem;