#ifndef _YOURAPI_LINK_CPP
#define _YOURAPI_LINK_CPP

#include "YourAPI_link.h"

using namespace std;

int function_main(PORISNode *mynode)
{
	int ret = EXIT_FAILURE;
	cout << "Executing function method with node " << mynode->name << endl;

	ret = EXIT_SUCCESS;
	return ret;
}

#endif //_YOURAPI_LINK_CPP
