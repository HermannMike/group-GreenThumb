import { useState, useEffect } from "react";

const PlantForm = ({ onSubmit, selectedPlant }) => {
  const [form, setForm] = useState({ name: "", type: "", lastWatered: "" });

  useEffect(() => {
    if (selectedPlant) setForm(selectedPlant);
  }, [selectedPlant]);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form);
    setForm({ name: "", type: "", lastWatered: "" });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} placeholder="Plant Name" required />
      <input name="type" value={form.type} onChange={handleChange} placeholder="Type" required />
      <input name="lastWatered" value={form.lastWatered} onChange={handleChange} placeholder="Last Watered Date" required />
      <button type="submit">{selectedPlant ? "Update" : "Add"} Plant</button>
    </form>
  );
};

export default PlantForm;