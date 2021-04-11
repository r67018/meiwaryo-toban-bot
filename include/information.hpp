#ifndef INFORMATION_HPP
#define INFORMATION_HPP

#include <map>
#include <string>
#define NAME_MODE_NUM 0
#define NAME_MODE_ALPHABET 1


namespace set {
    class information {
    private:
        int _name_mode;
        int _group_count;
        int _group_per_day;
        std::map<int, std::string> _groups;
    public:
        void setNameMode(int mode);
        int getNameMode();
        void setGroupCount(int n);
        int getGroupCount();
        void setGroupPerDay(int group_per_day);
        int getGroupPerDay();
        void createGroup();
        std::map<int, std::string> getGroup();
    };
}

#endif