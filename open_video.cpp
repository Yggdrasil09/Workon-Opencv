#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace cv;

int main(int argc,char** argv){
    namedWindow("Example",cv::WINDOW_AUTOSIZE);
    VideoCapture cap;
    cap.open("videos/sample.mp4");
    Mat frame;
    for(;;)
    {
        cap>>frame;
        if(frame.empty()) break;
        imshow("Example",frame);
        if(waitKey(33)>=0) break;
    }
    return 0;
}