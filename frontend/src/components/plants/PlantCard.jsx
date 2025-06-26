const PlantCard = ({ plant, onEdit, onDelete }) => ( 
  <div className="plant-card">
    <h3>{plant.name}</h3>
    <p>Type: {plant.type}</p>
    <p>Last Watered: {plant.lastWatered}</p>
    <button onClick={() => onEdit(plant)}>Edit</button>
    <button onClick={() => onDelete(plant.id)}>Delete</button>
  </div>
);

export default PlantCard;