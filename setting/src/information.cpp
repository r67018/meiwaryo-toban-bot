#include <iostream>
#include "../include/information.hpp"

void set::information::setNameMode(int name_mode)
{
    _name_mode = name_mode;
}

int set::information::getNameMode()
{
    return _name_mode;
}

void set::information::setGroupCount(int group_count)
{
    _group_count = group_count;
}

int set::information::getGroupCount()
{
    return _group_count;
}

void set::information::setGroupPerDay(int group_per_day)
{
    _group_per_day = group_per_day;
}

int set::information::getGroupPerDay()
{
    return _group_per_day;
}

void set::information::createGroup()
{
    std::cout << "グループに対応する名前を入力してください" << std::endl;
    std::cout << "一つのグループに複数人いる場合はカンマで区切ってください" << std::endl;
    for (int i = 0; i < _group_count; ++i) {
        int number = i + (_name_mode == NAME_MODE_NUM ? 1 : 'A');
        std::string name;
        if (_name_mode == NAME_MODE_NUM) {
            std::cout << number << ": ";
        } else if (_name_mode == NAME_MODE_ALPHABET) {
            std::cout << (char)number << ": ";
        }
        std::cin >> name;
        _groups[number] = name;
    }
}

std::map<int, std::string> set::information::getGroup()
{
    return _groups;
}
