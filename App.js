


// import React, { useState } from "react";
// import "./App.css";
// import Chart from "./chart";

// function App() {
//   const [form, setForm] = useState({
//     district: "",
//     rainfall: "",
//     temperature: "",
//     crop: "paddy",
//     water_usage: "high",
//   });

//   const [result, setResult] = useState(null);
//   const [history, setHistory] = useState([]);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState("");

//   const handleChange = (e) => {
//     setForm({ ...form, [e.target.name]: e.target.value });
//   };

//   const analyze = async () => {
//     setLoading(true);
//     setError("");
//     setResult(null);

//     try {
//       const res = await fetch("http://127.0.0.1:5000/analyze", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           ...form,
//           rainfall: Number(form.rainfall),
//           temperature: Number(form.temperature),
//         }),
//       });

//       const data = await res.json();
      
//       // Handle potential backend error response
//       if (data.error) {
//         setError(data.error);
//       } else {
//         setResult(data);
//         setHistory(prev => [
//           ...prev,
//           {
//             groundwater: data.groundwater_prediction,
//             rainfall: form.rainfall,
//             temperature: form.temperature,
//           }
//         ]);
//       }
//     } catch (err) {
//       setError("⚠️ Failed to connect to backend");
//     }

//     setLoading(false);
//   };

//   return (
//     /* We'll use a class instead of inline styles for better performance */
//     <div className="main-wrapper"
//     style={
//         backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(${process.env.PUBLIC_URL + '/bg.jpeg'})`,
//         backgroundSize: 'cover',
//         backgroundPosition: 'center',
//         backgroundAttachment: 'fixed',
//         display: 'flex',
//         flexDirection: 'column',
//         align-items: 'center',
//         justify-content: 'center',
//         minHeight: '100vh',
//         width: '100%'
//       }>
//       <div className="container">
//         <h1>💧 HydroGuard AI</h1>
//         <p className="subtitle">Predict. Prevent. Preserve Water.</p>

//         {/* FORM CARD */}
//         <div className="card">
//           <h2>Enter Details</h2>

//           <input
//             name="district"
//             placeholder="District (e.g. Ludhiana)"
//             onChange={handleChange}
//           />

//           <input
//             name="rainfall"
//             placeholder="Rainfall (mm)"
//             onChange={handleChange}
//           />

//           <input
//             name="temperature"
//             placeholder="Temperature (°C)"
//             onChange={handleChange}
//           />

//           <select name="crop" onChange={handleChange}>
//             <option value="paddy">Paddy</option>
//             <option value="wheat">Wheat</option>
//             <option value="cotton">Cotton</option>
//             <option value="sugarcane">Sugarcane</option>
//             <option value="maize">Maize</option>
//             <option value="potato">Potato</option>
//             <option value="kinnow (Citrus)">Kinnow (Citrus)</option>
//             <option value="litchi/fruits">Litchi/Fruits</option>
//           </select>

//           <select name="water_usage" onChange={handleChange}>
//             <option value="low">Low 💧</option>
//             <option value="medium">Medium 💧💧</option>
//             <option value="high">High 💧💧💧</option>
//           </select>

//           <button onClick={analyze} disabled={loading}>
//             {loading ? "Analyzing..." : "Analyze"}
//           </button>
//         </div>

//         {/* ERROR */}
//         {error && <p className="error-msg">{error}</p>}

//         {/* RESULT CARD */}
//         {result && (
//           <div className="result-card">
//             <div className="result-box">
//               <h3>💧 Groundwater Level</h3>
//               <p className="prediction-val">{result.groundwater_prediction}m</p>
//             </div>

//             <div className="result-box">
//               <h3>🌾 Recommended Crop</h3>
//               <p>{result.recommended_crop}</p>
//             </div>
//             <div className="result-box">
//               <h3>⚠️ Water Status</h3>
//               <p><strong>{result.status}</strong></p>
//             </div>
//           </div>
//         )}
        
//         {history.length > 0 && (
//           <div className="chart-container">
//              <Chart data={history} />
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
import "./App.css";
import Chart from "./chart";

function App() {
  const [form, setForm] = useState({
    district: "",
    rainfall: "",
    temperature: "",
    crop: "paddy",
    water_usage: "high",
  });

  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const analyze = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...form,
          rainfall: Number(form.rainfall),
          temperature: Number(form.temperature),
        }),
      });

      const data = await res.json();
      
      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
        setHistory(prev => [
          ...prev,
          {
            groundwater: data.groundwater_prediction,
            rainfall: form.rainfall,
            temperature: form.temperature,
          }
        ]);
      }
    } catch (err) {
      setError("⚠️ Failed to connect to backend");
    }

    setLoading(false);
  };

  return (
    <div className="main-wrapper"
      style={{
        /* FIXED: Added double curly braces and camelCase for CSS properties */
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(${process.env.PUBLIC_URL + '/bg.jpeg'})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundAttachment: 'fixed',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',    /* FIXED: camelCase */
        justifyContent: 'center', /* FIXED: camelCase */
        minHeight: '100vh',
        width: '100%'
      }}>
      <div className="container">
        <h1>💧 HydroGuard AI</h1>
        <p className="subtitle">Predict. Prevent. Preserve Water.</p>

        {/* FORM CARD */}
        <div className="card">
          <h2>Enter Details</h2>

          <input
            name="district"
            placeholder="District (e.g. Ludhiana)"
            onChange={handleChange}
          />

          <input
            name="rainfall"
            placeholder="Rainfall (mm)"
            onChange={handleChange}
          />

          <input
            name="temperature"
            placeholder="Temperature (°C)"
            onChange={handleChange}
          />

          <select name="crop" onChange={handleChange}>
            <option value="paddy">Paddy</option>
            <option value="wheat">Wheat</option>
            <option value="cotton">Cotton</option>
            <option value="sugarcane">Sugarcane</option>
            <option value="maize">Maize</option>
            <option value="potato">Potato</option>
            <option value="kinnow (Citrus)">Kinnow (Citrus)</option>
            <option value="litchi/fruits">Litchi/Fruits</option>
          </select>

          <select name="water_usage" onChange={handleChange}>
            <option value="low">Low 💧</option>
            <option value="medium">Medium 💧💧</option>
            <option value="high">High 💧💧💧</option>
          </select>

          <button onClick={analyze} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </div>

        {/* ERROR */}
        {error && <p className="error-msg">{error}</p>}

        {/* RESULT CARD */}
        {result && (
          <div className="result-card">
            <div className="result-box">
              <h3>💧 Groundwater Level</h3>
              <p className="prediction-val">{result.groundwater_prediction}m</p>
            </div>

            <div className="result-box">
              <h3>🌾 Recommended Crop</h3>
              <p>{result.recommended_crop}</p>
            </div>
            <div className="result-box">
              <h3>⚠️ Water Status</h3>
              <p><strong>{result.status}</strong></p>
            </div>
          </div>
        )}
        
        {history.length > 0 && (
          <div className="chart-container">
             <Chart data={history} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;