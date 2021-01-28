pragma solidity >=0.8.0 <=0.9.0;

contract Student {
    string surname = "";
    string name = "";
    string middle_name = "";
    string school = "";
    string private login = "";
    bytes32 private password;
    
    mapping(string => uint16) universities;
    mapping(string => string[]) specialties;
    uint16 sum_score = 0;
    uint16[] score;
    string[] subjects;
    
    constructor (string[] memory en_personal_data, uint16[] memory en_score, string[] memory en_subjects) {
        surname = en_personal_data[0];
        name = en_personal_data[1];
        middle_name = en_personal_data[2];
        school = en_personal_data[3];
        login = en_personal_data[4];
        password = keccak256(abi.encodePacked(en_personal_data[5]));

        for (uint i = 0; i < en_score.length; i++) {
            sum_score += en_score[i];
            score.push(en_score[i]);
            subjects.push(en_subjects[i]);
        }
    }
    
    function set_data(string[] memory en_uni, string[][] memory en_spec, string memory en_login, string memory en_password) public {
        require(keccak256(abi.encodePacked(en_login)) == keccak256(abi.encodePacked(login)));
        require(keccak256(abi.encodePacked(en_password)) == password);
        
        for (uint i = 0; i < en_spec.length; i++) {
            universities[en_uni[i]] = 5 - uint16(i);
            
            for (uint j = 0; j < en_spec[i].length; j++) {
                specialties[en_uni[i]].push(en_spec[i][j]);
            }
        }
    }
    
    function get_all_information_for_university (string memory en_uni) public view returns (string[3] memory, uint16, uint16[] memory, string[] memory, string[] memory) {
        string[3] memory personal_data = [surname, name, middle_name];
        
        return (personal_data, sum_score * universities[en_uni], score, subjects, specialties[en_uni]);
    }
}

contract University {
    mapping(string => address[]) students;
    mapping(string => uint16) amount;
    string[] specialties;
    
    constructor (string[] memory en_spec, uint16[] memory en_amount) {
        for (uint i = 0; i < en_spec.length; i++) {
            specialties.push(en_spec[i]);
            amount[en_spec[i]] = en_amount[i];
        }
    }
    
    function is_in_specialties (string memory en_str) private view returns(bool) {
        bool is_in = false;
                
        for (uint i = 0; i < specialties.length; i++) {
            if (keccak256(abi.encodePacked(specialties[i])) == keccak256(abi.encodePacked(en_str))) {
                is_in = true;
                break;
            }
        }
        
        return is_in;
    }
    
    function add_student (address en_student, string memory en_spec) public {
        require(is_in_specialties(en_spec));
        
        students[en_spec].push(en_student);
    }
    
    function get_all_students_for_speciality (string memory en_spec) public view returns(address[] memory) {
        return students[en_spec];
    }
}
