// This code is (c) 2021 cosmoBots.eu

#ifndef _PORIS_H
#define _PORIS_H

#include <iostream>
#include <list>
#include <iterator>
#include <string>

using namespace std;

class PORIS {
    public:
        int id;
        uint8_t idx;
        std::string ident;
        std::string name;
        std::string description;
        PORIS *parent;
        virtual ~PORIS() = default;
};

class PORISParam;
class PORISSys;

class PORISValue : public PORIS {
    public:
};

class PORISValueFloat : public PORISValue {
    public:
    double data;
    double min;
    double max;
    double default_data;    
    double setData(double value);
};

class PORISValueText : public PORISValue {
    public:
};

class PORISMode : public PORIS {
    public:
    std::list<PORISValue *> values;
    std::list<PORISMode *> submodes;

    PORISValue *getEligibleValue(PORISValue *v);
    PORISMode *getEligibleSubMode(PORISMode *m);
    uint8_t getEligibleValue(uint8_t idx);
    uint8_t getEligibleSubMode(uint8_t idx);
};

class PORISNode : public PORIS {
    public:
    std::list<PORISMode *> modes;
    PORISMode *selectedMode = NULL;

    void init(void);
    PORISMode *setEligibleMode(void);
    PORISMode *getEligibleMode(PORISMode *m);
    PORISMode *setMode(PORISMode *m);
    uint8_t getEligibleMode(uint8_t idx);
    uint8_t setMode(uint8_t idx);
    PORISNode getSubNodeFromName(string name);
};

class PORISParam : public PORISNode {
    public:
    std::list<PORISValue *> values;
    PORISValue *selectedValue = NULL;

    void init(void);

    PORISMode *setEligibleMode(void);    
    PORISValue *setEligibleValue(void);
    PORISMode *setMode(PORISMode *m);
    PORISValue *getEligibleValue(PORISValue *v);
    PORISValue *setValue(PORISValue *v);
    uint8_t setMode(uint8_t idx);    
    uint8_t getEligibleValue(uint8_t idx);
    uint8_t setValue(uint8_t idx);
};

class PORISSys : public PORISNode {
    public:
    std::list<PORISParam *> params;
    std::list<PORISSys *> subsystems;

    void init(void);
    PORISMode *setEligibleMode(void);    
    PORISMode *setMode(PORISMode *m);
    uint8_t setMode(uint8_t idx);
    PORISSys *getSubSystemFromName(string name);
    PORISParam *getSubParamFromName(string name);
    PORISSys *getDescendantFromName(string name);
    PORISParam *getDescendantParamFromName(string name);
};

#endif //_PORIS_H
