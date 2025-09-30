let di = document.querySelector('.border img'); 
        let pic = ['/static/image/img1.jpg', 
            '/static/image/img2.jpg','/static/image/img3.jpg',
            '/static/image/img4.jpg',
        '/static/image/img5.jpg']; 
        let pos = 0;

        setInterval(() => {
            pos = (pos + 1) % pic.length;
            di.src = pic[pos];
        }, 2000);