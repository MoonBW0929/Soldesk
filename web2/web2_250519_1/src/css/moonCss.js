import PropTypes from 'prop-types';

const MoonCss = (props) => {

    const css = {
        backgroundColor: props.bgc,
        color: props.c,
        width: props.w
    };

    return (
        <div>
            <table border="1" style={css}>
                <tr>
                    <td>{props.bgc}</td>
                </tr>
                <tr>
                    <td>{props.c}</td>
                </tr>
            </table>
        </div>
    );
};

MoonCss.prototype = {
    bgc : PropTypes.string.isRequired,
    c : PropTypes.string.isRequired
}

export default MoonCss;
