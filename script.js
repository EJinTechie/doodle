document.addEventListener('DOMContentLoaded', () => {
    const ghost = document.querySelector('.ghost');
    const leftEye = document.querySelector('.eye.left');
    const rightEye = document.querySelector('.eye.right');

    // 클릭 이벤트 리스너 추가
    ghost.addEventListener('click', () => {
        // 눈에 blink 클래스를 추가하여 깜빡임 효과를 생성
        leftEye.classList.toggle('blink');
        rightEye.classList.toggle('blink');
    });

    // 마우스 이동 이벤트 리스너 추가
    document.addEventListener('mousemove', (event) => {
        const funleft = 20; // 마우스 포인터와 유령 사이의 X축 거리
        const funtop = 20;  // 마우스 포인터와 유령 사이의 Y축 거리
        ghost.style.left = `${event.clientX + funleft}px`;
        ghost.style.top = `${event.clientY + funtop}px`;
    });
});
