# Detecting-packages

## 실행 준비
  $ pip install -r requirements.txt

필요한 패키지 다운로드
(좀 많이 설치해야 함)

## 실행
  $ python detect.py --source <이미지나 동영상> --weights best.pt
  
  
실행 결과는 runs/detect/ex{n} 경로로 저장됨

### 정보
실행하면 객체를 인식할 이미지나 동영상을 인식한 객체를 표시한 테두리와 함께 보여준다.

콘솔창에는 한 프레임당 인식한 객체의 라벨과 갯수, 실행 시간이 로그로 뜬다.

```python


  LOGGER.info(f'{s}Done. ({t3 - t2:.3f}s)')


```
로그 내용은 # Print results 에
