import click
import handler_video as hd
import control_aug as ctl

@click.command()
@click.option('--rotate','-r','control',flag_value='rotate',help='Rotate Augmentation.')
@click.option('--translate','-t','control',flag_value='translate', help='Translate Augmentation.')
@click.option('--input_video',help='Input video path.')
@click.option('--output_video',help='Output video path.')
@click.option('--degree','-d', help='Degree Rotate')
@click.option('--vector','-v', help='Vector Translate [x|y|x,y]')
@click.option('--axis','-a',type=click.Choice(['x','y','xy'],case_sensitive=False),help='Axis translate')
@click.option('--flip','-f' ,default=False, help='Flip translate')


def augmentation(input_video,output_video,control,degree,vector,axis,flip):
    
    if input_video is None or output_video is None or control is None:
        raise click.UsageError('Must be complete input_video, output video and control augmentation')

    frames,fps = hd.video2frame(input_video)

    if control == 'rotate': 
        if degree is None:
            raise click.UsageError('Must be fill degree value')

        frames_aug = [ctl.augmented_rotate(frame,float(degree)) for frame in frames]

    if control == 'translate' :
        if vector is None or axis is None:
            raise click.UsageError('Must be fill degree value')
        
        value = {
            'vector' : vector,
            'axis'   : axis,
            'flip'   : flip
        }
        frames_aug = [ctl.augmented_translate(frame,value) for frame in frames]

    hd.frame2video(frames_aug,fps,output_video)
        


if __name__ == "__main__":
    augmentation()

