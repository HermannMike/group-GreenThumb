import PlantList from "../components/plants/PlantList";

const PlantsPage = () => {
  return (
    <div className="plants-page">
      <h2>My Plants 🌿</h2>
      <p>Here you'll see your plants listed.</p>
      <PlantList />
    </div>
  );
};

export default PlantsPage;