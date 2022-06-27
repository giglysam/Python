import sys
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm


def main(argv):
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        colormap = mpl.cm.jet
        cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
        scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)
        colors = scalarMap.to_rgba(gray)
        blur = cv2.GaussianBlur(colors, (15, 15), 0)

        cv2.imshow('frame', blur)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
