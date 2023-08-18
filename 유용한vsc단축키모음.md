문서 작성 시 참고..를 가장한 인용 90% 영상 = https://youtu.be/mh-0twurNRE


Peek
F12를 누르면 해당 함수 정보? 창으로 이동하여 함수에 대한 정보를 보여줌. (뭐 들어가있는지 라던가)
이게 귀찮다 그러면 그냥 ALT + F12 눌러서 창 띄워가지고 거기서 수정도 가능함.
Refactoring
함수로 싸매기(?)
예를 들어 console.log(input.data)라고 한다 근데 이걸 함수로 바꾸고 싶으면 
해당 함수를 하이라이트(커서로 쭉 끌어서) Ctrl+Shift+R 해주면 Extract Function이라고 뜨면서 바로 함수로 바꿔준다.
스코프 안/밖 다 가능함.
그냥 변수만으로 제한되는 게 아니라 constant로 바꿀 수도 있다함.
너무 코드를 그지같이 짜서 스파게티 면마냥 길어가지고 파일로 나눠야겠다 싶으면
Ctrl+Shift+R 누르고 Move to a file 조져서 바로 새 파일로 옮길 수 잇음. 
Renam Symbol
변수 이름 바꾸기
이름 바꿀 변수 하이라이트 해주고 우클릭=>Rename Symbol 또는 F2 눌러주면 바뀜. 
(변수 참조시 참조된 파일까지 변수 이름을 싹 다 바꿔줌), Find and Replace 창 켜서 함수 이름 바꾸는 거보다 낫다. 효율적으로 살자...
+ Extension (Snippets)
내가 함수 별 자동완성을 너무 심하게 사용한다하면 쓰는 Extension인데 
사바사긴한데 자주 쓰는 코드를 작성시 일일이 타이핑 쳐줄 필요가 없음. 아마 기밀 문서 작성 시 사용하면 조지는 걸로 알고있으니 공용 / 공개 코드서만 사용하도록 합시다.
사용 예시 irr 치고 바로 뭐 하나 선택해주면 자주 쓰는 
import { BrowserRouter as Router, Route, NavLink } from 'react-router-dom' 코드가 자동완성됨. 예제 작성시 귀찮게 타이핑하지말고 Snippets 써주자.
- 사용 방법 : https://youtu.be/mh-0twurNRE?t=205 

사실 며칠만에 이렇게 미친듯이 공부해서 내가 리액트를 배웠다 하는 건 아니고 그냥 코딩애플 유튜브 보고 적었음.
코딩애플 구독. 솔직히 재밌음.
