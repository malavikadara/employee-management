const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export const employeeService = {
  // GET /employee/
  getAllEmployees: async () => {
    const response = await fetch(`${API_BASE_URL}/employee/`);
    if (!response.ok) throw new Error("Failed to fetch employees");
    return response.json();
  },

  // GET /employee/{employeeid}
  getEmployeeById: async (employeeId) => {
    const response = await fetch(`${API_BASE_URL}/employee/${employeeId}`);
    if (!response.ok) throw new Error(`Failed to fetch employee with ID ${employeeId}`);
    return response.json();
  },

  // POST /employee/
  createEmployee: async (employeeData) => {
    const response = await fetch(`${API_BASE_URL}/employee/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(employeeData),
    });
    if (!response.ok) throw new Error("Failed to create employee");
    return response.json();
  },

  // PUT /employee/{employeeid} (Full update)
  updateEmployeePut: async (employeeId, employeeData) => {
    const response = await fetch(`${API_BASE_URL}/employee/${employeeId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(employeeData),
    });
    if (!response.ok) throw new Error(`Failed to update employee with ID ${employeeId}`);
    return response.json();
  },

  // PATCH /employee/{employeeid} (Partial update)
  updateEmployeePatch: async (employeeId, partialData) => {
    const response = await fetch(`${API_BASE_URL}/employee/${employeeId}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(partialData),
    });
    if (!response.ok) throw new Error(`Failed to patch employee with ID ${employeeId}`);
    return response.json();
  },

  // DELETE /employee/{employeeid}
  deleteEmployee: async (employeeId) => {
    const response = await fetch(`${API_BASE_URL}/employee/${employeeId}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error(`Failed to delete employee with ID ${employeeId}`);
    return response.json();
  },
};