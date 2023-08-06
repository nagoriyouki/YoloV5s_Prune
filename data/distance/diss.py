public double sizeCompare(List<Detector.Recognition> recognitions) {

    Vector v = new Vector();

    if (recognitions != null) {
      // 사이즈 모두 계산, sorting 까지
      for (Detector.Recognition r : recognitions) {
        SizeNType temp = new SizeNType();#볼라드인지를 학인
        temp.size = Math.sqrt(r.getLocation().width() * r.getLocation().height()); #상크기 루트 씌운거
        temp.type = r.getTitle();
        // 같은 class 일 경우만 선정
        if (oldTitle != null) {
          if (temp.type.equals(oldTitle))
            v.add(temp);
        } else{ // 첫 시행이라 oldTitle이 null 일 때
          oldTitle = temp.type;
        }
      } #ratio계산

#인식한 객체들이 리스트로 들어와있으니 볼라드만 뽑아서 ratio를 구하는 코드

#가까워지는 경우
if(oldSqrSize < curr_squareSize)
        tempRatio = oldSqrSize * Math.pow(curr_squareSize, -1);

#멀어지는 경우
else if(oldSqrSize > curr_squareSize)
        tempRatio = -1 * curr_squareSize * Math.pow(oldSqrSize, -1);

#물체로부터의 거리 계산
double distanceFrom = 0;

#멀어질 경우 : 3/5 비교 후, => 보폭 * 5/2 => 보폭 * pow((1 - 3/5), -1)    (넘겨줄 때 음수 처리)
#가까워질 경우 : 3/5 비교 후, => 보폭 * 3/2 => 보폭 * 3/5 * pow((1 - 3/5), -1)

#ratio는 큰 거로 나누기

#가까워질 때
if(ratio > 0):
    distanceFrom = movedDistance * ratio * Math.pow((1 - ratio), -1);

#멀어질 때 그래서 음수로 바꿨다가 마지막 연산시에 다시 -1곱해서 원래대로 변환
else if (ratio < 0):
    ratio = -1 * ratio;
    distanceFrom = movedDistance * Math.pow((1 - ratio), -1);


#r1,r2 비교, 큰 쪽에서 작은 쪽을 나누기/멀어질때와 가까워질떄에 따라 공식을 따로 분할에서 사용   

