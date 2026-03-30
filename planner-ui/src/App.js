import { useState } from "react";

function App() {

  const [data, setData] = useState(null);

  const handleSubmit = async () => {
  try {
    const res = await fetch("http://127.0.0.1:5000/api", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        project_type: "final",
        team_size: 3,
        duration: 20,
        technology: "Python"
      })
    });

    const result = await res.json();
    console.log(result);
    setData(result);

  } catch (err) {
    console.error("ERROR:", err);
  }
};

  return (
    <div style={{background:"#0f2027",color:"#00ffe0",height:"100vh"}}>
      <h1>⚡ Planner UI</h1>
      <button onClick={handleSubmit}>Generate</button>

      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}

export default App;