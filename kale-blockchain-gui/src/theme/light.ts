import { createMuiTheme } from '@material-ui/core/styles';
import theme from './default';

export default (locale: object) =>
  createMuiTheme(
    {
      ...theme,
      palette: {
        ...theme.palette,
      },
    },
    locale,
  );
