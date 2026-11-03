import React, { useState, useEffect } from "react";
import { employeeService } from "./services/employeeService";
import "./App.css";

const initialFormState = {
  name: "",
  email: "",
  department: "",
  role: "",
  salary: "",
};

function App() {
  const [employees, setEmployees] = useState([]);
  const [formData, setFormData] = useState(initialFormState);
  const [editingId, setEditingId] = useState(null);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchEmployees = async () => {
    setLoading(true);
    try {
      const data = await employeeService.getAllEmployees();
      setEmployees(Array.isArray(data) ? data : []);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const payload = {
        ...formData,
        salary: Number(formData.salary),
      };

      if (editingId) {
        // Using PUT for updating an existing employee
        await employeeService.updateEmployeePut(editingId, payload);
      } else {
        // POST new employee
        await employeeService.createEmployee(payload);
      }

      setFormData(initialFormState);
      setEditingId(null);
      await fetchEmployees();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (employee) => {
    setEditingId(employee.id);
    setFormData({
      name: employee.name || "",
      email: employee.email || "",
      department: employee.department || "",
      role: employee.role || "",
      salary: employee.salary || "",
    });
  };

  const handleCancelEdit = () => {
    setEditingId(null);
    setFormData(initialFormState);
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this employee?")) return;
    setLoading(true);
    try {
      await employeeService.deleteEmployee(id);
      await fetchEmployees();
      if (selectedEmployee?.id === id) {
        setSelectedEmployee(null);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleView = async (id) => {
    try {
      const employee = await employeeService.getEmployeeById(id);
      setSelectedEmployee(employee);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <h1>Employee Management System</h1>

      {error && <div className="alert error">{error}</div>}

      {/* Form Section */}
      <div className="card">
        <h2>{editingId ? "Edit Employee" : "Add New Employee"}</h2>
        <form onSubmit={handleSubmit} className="employee-form">
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            value={formData.email}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="department"
            placeholder="Department"
            value={formData.department}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="role"
            placeholder="Role / Title"
            value={formData.role}
            onChange={handleInputChange}
            required
          />
          <input
            type="number"
            name="salary"
            placeholder="Salary"
            value={formData.salary}
            onChange={handleInputChange}
            required
          />
          <div className="form-actions">
            <button type="submit" disabled={loading}>
              {editingId ? "Update Employee" : "Create Employee"}
            </button>
            {editingId && (
              <button type="button" className="btn-cancel" onClick={handleCancelEdit}>
                Cancel
              </button>
            )}
          </div>
        </form>
      </div>

      {/* Detail Modal/Card */}
      {selectedEmployee && (
        <div className="card details-card">
          <h3>Employee Details (ID: {selectedEmployee.id})</h3>
          <p><strong>Name:</strong> {selectedEmployee.name}</p>
          <p><strong>Email:</strong> {selectedEmployee.email}</p>
          <p><strong>Department:</strong> {selectedEmployee.department}</p>
          <p><strong>Role:</strong> {selectedEmployee.role}</p>
          <p><strong>Salary:</strong> ${selectedEmployee.salary}</p>
          <button onClick={() => setSelectedEmployee(null)}>Close</button>
        </div>
      )}

      {/* Employee List Table */}
      <div className="card">
        <h2>Employee List</h2>
        {loading && <p>Loading...</p>}
        <table className="employee-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Department</th>
              <th>Role</th>
              <th>Salary</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {employees.length === 0 ? (
              <tr>
                <td colSpan="7" style={{ textAlign: "center" }}>No employees found.</td>
              </tr>
            ) : (
              employees.map((emp) => (
                <tr key={emp.id}>
                  <td>{emp.id}</td>
                  <td>{emp.name}</td>
                  <td>{emp.email}</td>
                  <td>{emp.department}</td>
                  <td>{emp.role}</td>
                  <td>${emp.salary}</td>
                  <td className="actions-cell">
                    <button className="btn-view" onClick={() => handleView(emp.id)}>View</button>
                    <button className="btn-edit" onClick={() => handleEdit(emp)}>Edit</button>
                    <button className="btn-delete" onClick={() => handleDelete(emp.id)}>Delete</button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;