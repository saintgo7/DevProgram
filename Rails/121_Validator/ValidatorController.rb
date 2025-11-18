class ValidatorController < ApplicationController
  before_action :set_validator, only: [:show, :edit, :update, :destroy]

  # GET /validator
  def index
    @validators = Validator.all
    render json: @validators
  end

  # GET /validator/1
  def show
    render json: @validator
  end

  # POST /validator
  def create
    @validator = Validator.new(validator_params)

    if @validator.save
      render json: @validator, status: :created
    else
      render json: @validator.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /validator/1
  def update
    if @validator.update(validator_params)
      render json: @validator
    else
      render json: @validator.errors, status: :unprocessable_entity
    end
  end

  # DELETE /validator/1
  def destroy
    @validator.destroy
    head :no_content
  end

  private

  def set_validator
    @validator = Validator.find(params[:id])
  end

  def validator_params
    params.require(:validator).permit(:name)
  end
end
