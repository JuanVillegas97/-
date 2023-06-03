#include <iostream>
#include <fstream>
#include <variant>
#include <string>
#include <vector>
#include "../headers/json.hpp"

using json = nlohmann::json;

struct Quadruple {
    int operator_;
    std::variant<int, std::string> left_operand;
    std::variant<int, std::string> right_operand;
    std::variant<int, std::string> avail;
};

// Helper function to convert variant to string
std::string variantToString(const std::variant<int, std::string>& value) {
    if (auto intValue = std::get_if<int>(&value)) {
        return std::to_string(*intValue);
    } else if (auto stringValue = std::get_if<std::string>(&value)) {
        return *stringValue;
    } else {
        return "Unknown";
    }
}

// Helper function to deserialize Quadruple from JSON
void from_json(const json& j, Quadruple& q) {
    q.operator_ = j["_Quadruple__operator"].get<int>();

    auto leftOperandValue = j["_Quadruple__left_operand"];
    if (leftOperandValue.is_number()) {
        q.left_operand = leftOperandValue.get<int>();
    } else if (leftOperandValue.is_string()) {
        q.left_operand = leftOperandValue.get<std::string>();
    } else {
        q.left_operand = "Unknown";
    }

    auto rightOperandValue = j["_Quadruple__right_operand"];
    if (rightOperandValue.is_number()) {
        q.right_operand = rightOperandValue.get<int>();
    } else if (rightOperandValue.is_string()) {
        q.right_operand = rightOperandValue.get<std::string>();
    } else {
        q.right_operand = "Unknown";
    }

    auto availValue = j["_Quadruple__avail"];
    if (availValue.is_number()) {
        q.avail = availValue.get<int>();
    } else if (availValue.is_string()) {
        q.avail = availValue.get<std::string>();
    } else {
        q.avail = "Unknown";
    }
}

// Function to deserialize JSON data and return vector of quadruples
std::vector<Quadruple> deserializeQuadruples(const std::string& filename) {
    std::vector<Quadruple> quadruples;

    // Read the JSON data from the file
    std::ifstream file(filename);
    json jsonData;
    file >> jsonData;

    // Access the "quadruples" array
    if (jsonData.contains("quadruples")) {
        json quadrupleData = jsonData["quadruples"];
        if (quadrupleData.is_array()) {
            for (const auto& quadruple : quadrupleData) {
                // Deserialize the quadruple from JSON
                Quadruple new_quadruple;
                from_json(quadruple, new_quadruple);

                // Add the quadruple to the vector
                quadruples.push_back(new_quadruple);
            }
        }
    }

    return quadruples;
}

// Function to print the quadruple properties
void printQuadruples(const std::vector<Quadruple>& quadruples) {
    for (const auto& quadruple : quadruples) {
        std::cout << "Operator: " << quadruple.operator_ << ", "
                  << "Left Operand: " << variantToString(quadruple.left_operand) << ", "
                  << "Right Operand: " << variantToString(quadruple.right_operand) << ", "
                  << "Avail: " << variantToString(quadruple.avail) << std::endl;
    }
}

int main() {
    std::string filename = "data.json";

    // Deserialize the quadruples from the JSON file
    std::vector<Quadruple> quadruples = deserializeQuadruples(filename);

    // Print the quadruple properties
    printQuadruples(quadruples);

    return 0;
}
