const Alert = ({ message, type = "info" }) => {
  const colors = {
    success: "green",
    error: "red",
    info: "blue",
  };

  return (
    <div style={{
      backgroundColor: colors[type] + "20",
      border: `1px solid ${colors[type]}`,
      padding: "10px",
      borderRadius: "5px",
      marginBottom: "10px",
    }}>
      <strong>{type.toUpperCase()}:</strong> {message}
    </div>
  );
};

export default Alert;