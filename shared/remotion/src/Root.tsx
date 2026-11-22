import React from 'react';
import {Composition, Still} from 'remotion';
import {Reel, ReelProps, reelDuration} from './Reel';
import {Slide, SlideProps} from './Slide';
import {Film, FilmProps, filmDuration} from './Film';
const demoReel: ReelProps = {brand: 'vanxcel', hook: 'Demo', scenes: [{type: 'title', dur: 2, title: 'Demo'}, {type: 'end', dur: 2, title: 'Einde'}]};
const demoSlide: SlideProps = {brand: 'vanxcel', layout: 'statement', title: 'Demo'};
export const Root: React.FC = () => <>
  <Composition id="Reel" component={Reel as any} width={1080} height={1920} fps={30} durationInFrames={120} defaultProps={demoReel}
    calculateMetadata={({props}) => ({durationInFrames: reelDuration(props as ReelProps, 30)})} />
  <Composition id="Film" component={Film as any} width={1080} height={1920} fps={30} durationInFrames={120} defaultProps={{brand: 'loveke', shots: []} as FilmProps}
    calculateMetadata={({props}) => ({durationInFrames: Math.max(30, filmDuration(props as FilmProps, 30))})} />
  <Still id="Slide" component={Slide as any} width={1080} height={1350} defaultProps={demoSlide} />
  <Still id="Story" component={Slide as any} width={1080} height={1920} defaultProps={demoSlide} />
</>;
