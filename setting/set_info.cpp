#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include "../include/information.hpp"


int main()
{
    // get local time
    time_t t = std::time(nullptr);
    const tm* lt = std::localtime(&t);

    // convert to string
    std::string year = "20";
    year += std::to_string(lt->tm_year - 100);
    std::string month = std::to_string(lt->tm_mon);
    std::string day = std::to_string(lt->tm_mday);

    // write date to the files
    std::string path;

    path = "../src/info/year.txt";
    std::ofstream year_txt(path);
    year_txt << year;

    path = "../src/info/month.txt";
    std::ofstream month_txt(path);
    month_txt << month;

    path = "../src/info/day.txt";
    std::ofstream day_txt(path);
    day_txt << day;

    // input information
    set::information info;
    std::cout << "グループの個数は何個ですか" << std::endl;
    int group_count;
    do {
        std::cout << ">> ";
        std::cin >> group_count;
    } while (group_count <= 0);
    info.setGroupCount(group_count);

    std::cout << "1日当たりのグループ数は何個ですか" << std::endl;
    int group_per_day;
    std::cout << ">> ";
    std::cin >> group_per_day;

    std::cout << "グループ名は数字ですか、アルファベットですか" << std::endl;
    std::cout << "0: 数字, 1: アルファベット" << std::endl;
    int name_mode;
    do {
        if (info.getGroupCount() >= 28) {
            std::cout << "グループ数が28個以上のため、自動的に数字が選択されます" << std::endl;
            name_mode = NAME_MODE_NUM;
            break;
        }
        std::cout << ">> ";
        std::cin >> name_mode;
    } while (name_mode != 0 && name_mode != 1);
    info.setNameMode(name_mode);

    // write today group
    std::cout << "今日のグループは何ですか" << std::endl;
    std::string today_group;
    std::cout << ">> ";
    std::cin >> today_group;
    path = "../src/info/group.txt";
    std::ofstream group_txt(path);
    group_txt << today_group;

    info.createGroup();

    // write into src/group_config.py
    path = "../src/group_config.py";
    std::ofstream group_config_py(path);
    std::stringstream main_group;
    main_group << "main_group = [";
    for (int i = 0; i < group_count; ++i) {
        if (name_mode == NAME_MODE_NUM) {
            main_group << i + 1;
        } else if (name_mode == NAME_MODE_ALPHABET) {
            main_group << "'" << char('A' + i) << "'";
        }
        main_group << ", ";
    }
    main_group << "]\n";
    group_config_py << main_group.str();


    std::stringstream name;
    name << "name = {";
    std::map<int, std::string> groups = info.getGroup();
    for (auto& group : groups) {
        if (name_mode == NAME_MODE_NUM) {
            name << group.first;
        } else if (name_mode == NAME_MODE_ALPHABET) {
            name << "'" << char(group.first) << "'";
        }
        name << ": " << group.second << ", ";
    }
    name << "}\n";
    group_config_py << name.str();

    std::string group_per_day_str = "group_per_day = " + std::to_string(group_per_day) + "\n";
    group_config_py << group_per_day_str;

    std::string group_size_str = "group_size = len(main_group)\n";
    group_config_py << group_size_str;
}
