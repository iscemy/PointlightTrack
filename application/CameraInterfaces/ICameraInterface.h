
#include "CameraInitParams.h"

class ICameraInterface {
    public:
    virtual int GetImage(uint8_t *pBuffer, int bufferSize) = 0;
    virtual int InitCamera(CCameraInitParams initParams) = 0;
};