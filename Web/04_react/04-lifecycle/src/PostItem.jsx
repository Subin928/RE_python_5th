// 실습 2 - jsonplaceholder 사이트로 API 요청 보내기
// 01
// 이전 실습에서 로컬의 데이터를 호출한 것을 jsonplaceholder 사이트로 요청 보내서 가져오기 (= fetch 혹은 axios 사용하기)
// npm i axios # axios 사용할 경우, 모듈 설치 필요
// fetch와 axios는 프로미스 기반임을 주의할 것 (async/await)
// jsonplaceholder로 요청할 때 요청 방식은 당연히 GET 이겠죠?

function PostItem({ post }) {
	return (
		<div className='PostItem'>
			<div>
				<span className='id'>No. {post.id}</span>
				<span className='title'>- {post.title}</span>
			</div>
			<p className='body'>{post.body.slice(0, 120)}...</p>
		</div>
	);
}

export default PostItem;
