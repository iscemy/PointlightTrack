
#include "string"

enum class CameraInterfaceType {
    udp,
};

struct CCameraInitParams {
    public:
    CameraInterfaceType type;
    float exptectedFrameRate;
    std::string sourceIpAddress;
    std::string sourceFolder;
    std::string fileNamePrefix, fileNameSuffix;
    int folderImageStartOffset;
    uint16_t sourcePort;
    int imageWidth, imageHeight, imageDepth;

};