import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as KaleIcon } from './images/kale.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={KaleIcon} viewBox="0 0 150 58" {...props} />;
}
