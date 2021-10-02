package com.example.happybirthday;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;

public class SecondActivity extends AppCompatActivity {


    private MediaPlayer mediaPlayer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate (savedInstanceState);
        setContentView ( R.layout.activity_second );

        mediaPlayer = MediaPlayer.create ( SecondActivity.this,R.raw.play  );
        mediaPlayer.setLooping ( true );
        mediaPlayer.start ();



    }

    @Override
    protected void onResume()  {
        super.onResume ();
        mediaPlayer.start ();

    }
    @Override
    protected void onPause() {
        super.onPause ();
        mediaPlayer.pause ();
    }
    @Override
    protected void onDestroy() {
        super.onDestroy ();
        mediaPlayer.start ();
        mediaPlayer.release ();
    }

    }
