package com.example.happybirthday;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Handler;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private static int SPLASH_TIME_OUT = 5000;

    ImageView background, date, bgirl ;
    TextView september, happy;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate (savedInstanceState);
        setContentView (R.layout.activity_main);

        background = findViewById (R.id.img);
        date = findViewById (R.id.img1);
        september = findViewById (R.id.sep);
        happy =findViewById (R.id.hb);
        bgirl = findViewById ( R.id.img2 );


        background.animate ().translationY (-2200).setDuration (1000).setStartDelay (4000);
        date.animate ().translationY (2000).setDuration (1000).setStartDelay (4000);
        september.animate ().translationY (2000).setDuration (1000).setStartDelay (4000);
        happy.animate ().translationY (2000).setDuration (1000).setStartDelay (4000);
        bgirl.animate ().translationY (2000).setDuration (1000).setStartDelay (4000);







        new Handler ().postDelayed ( new Runnable () {
            @Override
            public void run() {
                Intent intent = new Intent (MainActivity.this, SecondActivity.class);
                startActivity ( intent );
                finish ();





            }


        },SPLASH_TIME_OUT );




    }
}