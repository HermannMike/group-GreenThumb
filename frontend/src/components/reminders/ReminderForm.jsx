import { useState } from "react";

const ReminderForm = ({ onAdd }) => {
  const [form, setForm] = useState({ text: "", date: "" });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd({ ...form, id: Date.now() });
    setForm({ text: "", date: "" });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="text" value={form.text} onChange={handleChange} placeholder="Reminder Text" required />
      <input name="date" type="date" value={form.date} onChange={handleChange} required />
      <button type="submit">Add Reminder</button>
    </form>
  );
};

export default ReminderForm;
