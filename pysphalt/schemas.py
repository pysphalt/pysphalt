from pydantic import BaseModel, Field


class AsphaltMixInputs(BaseModel):
    frequency: float = Field(..., description="Frequency in Hz")
    binder_dynamic_shear_modulus: float = Field(
        ..., description="Binder dynamic shear modulus at 20°C in psi"
    )
    binder_phase_angle: float = Field(
        ..., description="Binder phase angle at 20°C in degrees"
    )
    aggregates_passing_sieve_200: float = Field(
        ..., description="Aggregates passing sieve No. 200 in percentage"
    )
    retained_material_sieve_4: float = Field(
        ..., description="Cumulative retained material on sieve No. 4 in percentage"
    )
    retained_material_sieve_8: float = Field(
        ..., description="Cumulative retained material on sieve 8” in percentage"
    )
    retained_material_sieve_3_4: float = Field(
        ..., description="Cumulative retained material on sieve 3/4” in percentage"
    )
    air_voids: float = Field(..., description="Air voids in percentage")
    effective_binder_volume: float = Field(
        ..., description="Effective binder volume in percentage"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "frequency": 1.0,
                "binder_dynamic_shear_modulus": 500,
                "binder_phase_angle": 5,
                "aggregates_passing_sieve_200": 10.0,
                "retained_material_sieve_4": 15.0,
                "retained_material_sieve_8": 20.0,
                "retained_material_sieve_3_4": 25.0,
                "air_voids": 5.0,
                "effective_binder_volume": 12.0,
            }
        }
