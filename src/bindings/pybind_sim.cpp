#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <random>

namespace py = pybind11;

struct EmployeeData {
    int id;
    double corporate_capital;
    int department_id;
};

// Reescribimos la simulación para que devuelva los datos directo a la RAM de Python
std::vector<EmployeeData> run_rae_simulation(int num_agents, double initial_capital, int iterations) {
    std::vector<EmployeeData> employees;
    employees.reserve(num_agents);
    
    for (int i = 0; i < num_agents; ++i) {
        int dept = (i % 5) + 1;
        employees.push_back({i, initial_capital, dept});
    }

    std::mt19937 rng(42); // Semilla fija para reproducibilidad en pruebas
    std::uniform_int_distribution<int> agent_dist(0, num_agents - 1);
    std::uniform_real_distribution<double> fraction_dist(0.0, 1.0);

    for (int iter = 0; iter < iterations; ++iter) {
        int i = agent_dist(rng);
        int j = agent_dist(rng);
        while (i == j) { j = agent_dist(rng); }

        double pool = employees[i].corporate_capital + employees[j].corporate_capital;
        double share = fraction_dist(rng);

        employees[i].corporate_capital = pool * share;
        employees[j].corporate_capital = pool * (1.0 - share);
    }
    return employees;
}

PYBIND11_MODULE(dark_agency, m) {
    m.doc() = "Dark Agency C++ Simulation Engine for Organizational Dynamics";

    py::class_<EmployeeData>(m, "EmployeeData")
        .def_readonly("id", &EmployeeData::id)
        .def_readonly("corporate_capital", &EmployeeData::corporate_capital)
        .def_readonly("department_id", &EmployeeData::department_id);

    m.def("run_rae_simulation", &run_rae_simulation, 
          "Run the Random Asset Exchange (RAE) model for HR",
          py::arg("num_agents"), py::arg("initial_capital"), py::arg("iterations"));
}
