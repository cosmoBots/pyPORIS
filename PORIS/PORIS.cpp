// This code is (c) 2021 cosmoBots.eu

#ifndef _PORIS_CPP
#define _PORIS_CPP

#include "PORIS.h"
#include <iostream>
#include <list>
#include <iterator>
#include <string>
#include <typeinfo>

using namespace std;

/////////////  Initialization routines ////////////////

void PORISNode::init(void){
    cout << "Init de " << this->name << ", número de modos: " << modes.size() << endl;
    PORISMode *firstMode = modes.front();
    cout << "Init " << this->name << ": " << firstMode->name << endl;
    setMode(firstMode);
};

/////////////  PORISMode routines ////////////////

PORISValue *PORISMode::getEligibleValue(PORISValue *v){
    if (v != NULL){
        cout << "Entro en PORISMode getEligibleValue para el modo " << this->name << " con valor propuesto " << v->name << endl;
    } else {
        cout << "Entro en PORISMode getEligibleValue para el modo " << this->name << " con valor propuesto NULO" << endl;
    }
   PORISValue *ret = NULL;
    list<PORISValue *> :: iterator it;
    bool found = false;
    for (it = values.begin();
        !found && it != values.end();++it){
        if (ret == NULL){
            ret = *it;
            cout << "Ponemos el primer valor eligible que encontramos " << ret->name << endl;
        }
        if (v != NULL){
            if (v->id == (*it)->id){
                ret = v;
                cout << "Ponemos el valor propuesto " << ret->name << endl;
                found = true;
            }
        }
    }
    return ret;
};

uint8_t PORISMode::getEligibleValue(uint8_t idx){
    auto l_front = values.begin();
    advance(l_front, idx);
    PORISValue *result = getEligibleValue(*l_front);
    if (result == NULL){
        return 0;
    } else {
        return result->idx;
    }
};

PORISMode * PORISMode::getEligibleSubMode(PORISMode *m){
    cout << "Entro en PORISMode getEligibleSubMode para el modo " << this->name << " con m = " << m->name << endl;
    PORISMode *ret = NULL;
    list<PORISMode *> :: iterator it;
    bool found = false;
    for (it = submodes.begin();
            !found && it != submodes.end();++it){
                //cout << "Itero con el submodo " << (*it)->name;
                //cout << " Los padres son " << (*it)->parent->name << " y " << m->parent->name << endl;
        if ((*it)->parent->id == m->parent->id){
            //cout << "El padre coincide ";
            if (ret == NULL){
                ret = *it;
                cout << " Me lo apunto: " << (*it)->name << endl;
            }
            if (m->id == (*it)->id){
                cout << " Nos coincide con 'm', lo podemos escoger!!! : " << (*it)->name << endl;
                ret = m;
                found = true;
            }
        }
    }
    cout << "No encontre nada " << endl;
    return ret;
};

uint8_t PORISMode::getEligibleSubMode(uint8_t idx){
    auto l_front = submodes.begin();
    advance(l_front, idx);
    PORISMode *result = getEligibleSubMode(*l_front);
    if (result == NULL){
        return 0;
    } else {
        return result->idx;
    }
};

/////////////  PORISNode routines ////////////////

PORISMode *PORISNode::getEligibleMode(PORISMode *m){
    cout << "Entro en PORISNode "<< this->name <<".getEligibleMode(" << m->name << ")" << endl;
    PORISMode *ret = NULL;
    if (parent == NULL){
        cout << "El padre de "<< this->name <<" es nulo" << endl;
        ret = m;
    } else {
        cout << "Buscamos entre los " << ((PORISNode*)parent)->selectedMode->submodes.size() << " submodos de " << parent->name << endl;
        ret = ((PORISNode*)parent)->selectedMode->getEligibleSubMode(m);
    }
    if (ret == NULL){
        cout << "No hubo suerte, el modo a seleccionar es nulo" << endl;
    } else {
        cout << "El modo seleccionado es " << ret->name << endl;
    }
    
    return ret;
};

uint8_t PORISNode::getEligibleMode(uint8_t idx){
    auto l_front = modes.begin();
    advance(l_front, idx);
    PORISMode *result = getEligibleMode(*l_front);
    cout << "Vamos 1" << endl;
    if (result == NULL) {
        return 0;
    } else {
        return result->idx;
    }
};

PORISMode *PORISNode::setEligibleMode(void){
    cout << "Entro en PORISNode setEligibleMode " << this->name << endl;
    if (selectedMode == NULL){
        this->init();
    }
    cout << "selectedMode es " << selectedMode->name << endl;
    
    PORISMode *ret = setMode(selectedMode);
    return ret;
};

uint8_t PORISNode::setMode(uint8_t idx){
    uint8_t ret = 0;
    auto l_front = modes.begin();
    advance(l_front, idx);
    PORISMode *result = setMode(*l_front);
    if (result == NULL){
        ret = 0;
    } else {
        ret = result->idx;
    }
    cout << "Acaba la operación setMode con resultado " << (int)ret << endl;      
    return ret;
}

/////////////  PORISSys routines ////////////////

PORISMode* PORISSys::setMode(PORISMode *m){
    cout << "Entro en Sys setMode de " << this->name;
    cout << " con modo " << m->name << endl;
    PORISMode *ret = getEligibleMode(m);
        cout << "Vamos 2" << endl;
    if (ret == NULL){
        cout << "el nuevo modo es NULO que es diferente del seleccionado ";
        cout << " Hemos de poner el modo UNKNOWN, que por defecto es el primero " << endl;
        ret = this->modes.front();
    }
    if (ret != selectedMode){
        cout << "el nuevo modo es " << ret->name;
        if (selectedMode != NULL) {
            cout << " que es diferente de " << selectedMode->name << endl;
        } else {
            cout << " que es diferente de NULO" << endl;
        }
        selectedMode = ret;
        list<PORISParam *> :: iterator itparam;
        for (itparam = params.begin(); itparam != params.end();++itparam){
            //cout << "Voy a iterar el param " << (*itparam)->name << endl;
            (*itparam)->setEligibleMode();
        }
        list<PORISSys *> :: iterator itsys;
        for (itsys = subsystems.begin(); itsys != subsystems.end();++itsys){
            (*itsys)->setEligibleMode();
            //cout << "Voy a iterar el sistema " << (*itsys)->name << endl;
        }                
    } else {
        cout << "El modo escogido es el mismo " << ret->name << endl;
    }
    cout << "Salgo de Sys setMode de " << this->name << " con m=" << m->name << " y resultado = " << ret->name << endl;
    return ret;
}

/////////////  PORISParam routines ////////////////

PORISValue *PORISParam::getEligibleValue(PORISValue *v){
    if (v == NULL){
        cout << "Entro en PORISParam getEligibleValue " << this->name << " con valor NULO " << endl;
    } else {
        cout << "Entro en PORISParam getEligibleValue " << this->name << " con valor " << v->name << endl;
    }
    PORISValue *ret = NULL;
    if (selectedMode == NULL){
        cout << " selectedMode es NULO";
        init();
    }  
    ret = selectedMode->getEligibleValue(v);
    return ret;
};


uint8_t PORISParam::getEligibleValue(uint8_t idx){
    auto l_front = values.begin();
    advance(l_front, idx);
    PORISValue *result = getEligibleValue(*l_front);
    if (result == NULL){
        return 0;
    } else {
        cout << "FIN: Vamos a retornar el valor " << result->name << endl;
        return result->idx;
    }  
};

PORISValue* PORISParam::setValue(PORISValue *v){
    if (v == NULL){
        cout << "Entro en PORISParam setValue " << this->name << " con valor NULO " << endl;
    } else {
        cout << "Entro en PORISParam setValue " << this->name << " con valor " << v->name << endl;
    }
    PORISValue *ret = getEligibleValue(v);
    if (ret != selectedValue){
        selectedValue = ret;
    }
    return ret;
};

uint8_t PORISParam::setValue(uint8_t idx){
    auto l_front = values.begin();
    advance(l_front, idx);
    PORISValue *result = setValue(*l_front);
    if (result == NULL){
        return 0;
    } else {
        return result->idx;
    }
};

PORISValue* PORISParam::setEligibleValue(void){
    cout << "Entro en PORISParam setEligibleValue " << this->name << endl;
    return setValue(selectedValue);
};

PORISMode* PORISParam::setMode(PORISMode *m){

    cout << "Entro en Param " << this->name << ".setMode(" << m->name << ")" << endl;
    PORISMode *ret = getEligibleMode(m);

    if (ret == NULL){
        ret = this->modes.front();
    }
    if (ret != selectedMode){
        selectedMode = ret;
        setValue(selectedValue);
    }
    return ret;
};

double PORISValueFloat::setData(double floatdata){
    cout << "Applying " << floatdata << " name: " << name << " min: " << min << " max: " << max << endl;
    if (floatdata >= min){
        if (floatdata <= max){
            data = floatdata;
        }
    }
    
    return data;
}


PORISSys *PORISSys::getSubSystemFromName(string name) {
    for (auto s:subsystems){
        if (s->name == name){
            return s;
        }
    }
    return NULL;
}

PORISParam *PORISSys::getSubParamFromName(string name) {
    for (auto p:params){
        if (p->name == name){
            return p;
        }
    }
    return NULL;
}

PORISSys *PORISSys::getDescendantFromName(string name) {
    PORISSys *ret = getSubSystemFromName(name);
    if (ret == NULL){
        for (auto s:subsystems){
            ret = s->getDescendantFromName(name);
            if (ret != NULL){
                return ret;
            }
        }
    }
    return ret;
}

PORISParam *PORISSys::getDescendantParamFromName(string name) {   
    PORISParam *ret = getSubParamFromName(name);
    if (ret == NULL){
        for (auto s:subsystems){
            ret = s->getDescendantParamFromName(name);
            if (ret != NULL){
                return ret;
            }
        }
    }
    return ret;
}

#endif //_PORIS_CPP
