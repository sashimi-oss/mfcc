let mediaRecorder;
    const chunks = [];

    function startRecording(stream) {
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunks.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'audio/wav' });
        saveBlobAsWavFile(blob, 'recorded.wav');
      };

      mediaRecorder.start();
    }

    function saveBlobAsWavFile(blob, filename) {
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename || 'audio.wav';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    document.getElementById('startRecording').addEventListener('click', () => {
      // メディアデバイスへのアクセス許可を取得
      navigator.mediaDevices.getUserMedia({ audio: true, video: false })
        .then((stream) => {
          // 録音を開始
          startRecording(stream);

          // 一定時間後に録音を停止する例
          setTimeout(() => {
            mediaRecorder.stop();
          }, 5000); // 5秒後に録音を停止
        })
        .catch((error) => {
          console.error("メディアデバイスへのアクセスが拒否されました。", error);
        });
    });