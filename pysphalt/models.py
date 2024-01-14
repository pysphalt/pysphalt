from typing import List
from pysphalt.schemas import AsphaltMixInputs
import pickle
import os

PICKLE_MODELS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "pickle_models"
)


class AsphaltModulusPredictor:
    """
    A predictive model for estimating the dynamic modulus (\|E*|\) of Brazilian asphalt mixtures using artificial neural networks (ANNs).

    This class implements an ANN-based approach to predict the dynamic modulus of asphalt mixtures, tailored to the specific characteristics and compositions typical of Brazilian formulations. It takes into account factors such as aggregate type, asphalt binder content, and environmental conditions, as described in the referenced study.

    The model is trained on empirical data from Brazilian asphalt mixture tests, aiming to provide accurate and reliable modulus predictions for use in pavement design and analysis.

    Methods:
        predict(inputs): Accepts input parameters of the asphalt mixture and returns the predicted dynamic modulus.

    Example:
        >>> predictor = AsphaltModulusPredictor()
        >>> modulus = predictor.predict([ ... ])
    """

    _loaded_model: object

    def __init__(self):
        # this_dir = os.path.dirname(os.path.abspath(__file__))
        pickle_path = os.path.join(PICKLE_MODELS_DIR, "asphalt_modulus_predictor.pkl")
        with open(pickle_path, "rb") as model_file:
            self._loaded_model = pickle.load(model_file)

    def predict(self, X: List[AsphaltMixInputs]) -> float:
        """
        Predicts the dynamic modulus of an asphalt mixture based on the given input parameters.

        Parameters
        ----------
        X : AsphaltMixInputs or array-like of shape (n_samples, n_features)
            Input data for prediction. Each instance of AsphaltMixInputs represents one sample of asphalt mixture,
            with the following features:

            - `frequency` (float): Frequency in Hz.
            - `binder_dynamic_shear_modulus` (float): Binder dynamic shear modulus at 20°C in psi.
            - `binder_phase_angle` (float): Binder phase angle at 20°C in degrees.
            - `aggregates_passing_sieve_200` (float): Aggregates passing sieve No. 200 in percentage.
            - `retained_material_sieve_4` (float): Cumulative retained material on sieve No. 4 in percentage.
            - `retained_material_sieve_8` (float): Cumulative retained material on sieve 8” in percentage.
            - `retained_material_sieve_3_4` (float): Cumulative retained material on sieve 3/4” in percentage.
            - `air_voids` (float): Air voids in percentage.
            - `effective_binder_volume` (float): Effective binder volume in percentage.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            The predicted dynamic modulus (\|E*\|) values for each asphalt mixture sample.

        Examples
        --------
        >>> predictor = AsphaltModulusPredictor()
        >>> inputs = AsphaltMixInputs(frequency=1.0, binder_dynamic_shear_modulus=500, ...)
        >>> y_pred = predictor.predict([inputs])
        """
        return self._loaded_model.predict(X)  # type: ignore[attr-defined]
