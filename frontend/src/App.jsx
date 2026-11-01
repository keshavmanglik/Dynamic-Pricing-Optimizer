import { useState } from "react";
import Papa from "papaparse";

function App() {
  const [fileName, setFileName] = useState("");
  const [data, setData] = useState([]);

  const [productColumn, setProductColumn] = useState("");
  const [priceColumn, setPriceColumn] = useState("");
  const [quantityColumn, setQuantityColumn] = useState("");
  const [dateColumn, setDateColumn] = useState("");
  const [categoryColumn, setCategoryColumn] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setFileName(file.name);

      Papa.parse(file, {
        header: true,
        skipEmptyLines: true,

        complete: (results) => {
          setData(results.data);

          // Reset previous mappings
          setProductColumn("");
          setPriceColumn("");
          setQuantityColumn("");
          setDateColumn("");
          setCategoryColumn("");
        },
      });
    }
  };

  const columns = data.length > 0 ? Object.keys(data[0]) : [];

  return (
    <div>
      <h1>Dynamic Pricing Strategy Optimizer</h1>

      <p>
        Upload your business data to analyze sales, demand and pricing.
      </p>

      <h2>Upload Dataset</h2>

      <input
        type="file"
        accept=".csv"
        onChange={handleFileChange}
      />

      {fileName && (
        <p>
          <strong>Uploaded File:</strong> {fileName}
        </p>
      )}

      {data.length > 0 && (
        <div>
          <h2>Dataset Preview</h2>

          <p>
            <strong>Total Records:</strong> {data.length}
          </p>

          <table border="1">
            <thead>
              <tr>
                {columns.map((column) => (
                  <th key={column}>{column}</th>
                ))}
              </tr>
            </thead>

            <tbody>
              {data.slice(0, 10).map((row, index) => (
                <tr key={index}>
                  {columns.map((column) => (
                    <td key={column}>{row[column]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>

          <hr />

          <h2>Data Mapping</h2>

          <p>
            Tell the system which columns represent each business field.
          </p>

          <div>
            <label>Product / SKU: </label>

            <select
              value={productColumn}
              onChange={(e) => setProductColumn(e.target.value)}
            >
              <option value="">Select column</option>

              {columns.map((column) => (
                <option key={column} value={column}>
                  {column}
                </option>
              ))}
            </select>
          </div>

          <br />

          <div>
            <label>Price: </label>

            <select
              value={priceColumn}
              onChange={(e) => setPriceColumn(e.target.value)}
            >
              <option value="">Select column</option>

              {columns.map((column) => (
                <option key={column} value={column}>
                  {column}
                </option>
              ))}
            </select>
          </div>

          <br />

          <div>
            <label>Quantity / Demand: </label>

            <select
              value={quantityColumn}
              onChange={(e) => setQuantityColumn(e.target.value)}
            >
              <option value="">Select column</option>

              {columns.map((column) => (
                <option key={column} value={column}>
                  {column}
                </option>
              ))}
            </select>
          </div>

          <br />

          <div>
            <label>Date: </label>

            <select
              value={dateColumn}
              onChange={(e) => setDateColumn(e.target.value)}
            >
              <option value="">Select column</option>

              {columns.map((column) => (
                <option key={column} value={column}>
                  {column}
                </option>
              ))}
            </select>
          </div>

          <br />

          <div>
            <label>Category: </label>

            <select
              value={categoryColumn}
              onChange={(e) => setCategoryColumn(e.target.value)}
            >
              <option value="">Select column</option>

              {columns.map((column) => (
                <option key={column} value={column}>
                  {column}
                </option>
              ))}
            </select>
          </div>

          <br />

          <button>
            Continue to Analysis
          </button>
        </div>
      )}
    </div>
  );
}

export default App;