class ValidationController < ApplicationController
  before_action :set_validation, only: [:show, :edit, :update, :destroy]

  # GET /validation
  def index
    @validations = Validation.all
    render json: @validations
  end

  # GET /validation/1
  def show
    render json: @validation
  end

  # POST /validation
  def create
    @validation = Validation.new(validation_params)

    if @validation.save
      render json: @validation, status: :created
    else
      render json: @validation.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /validation/1
  def update
    if @validation.update(validation_params)
      render json: @validation
    else
      render json: @validation.errors, status: :unprocessable_entity
    end
  end

  # DELETE /validation/1
  def destroy
    @validation.destroy
    head :no_content
  end

  private

  def set_validation
    @validation = Validation.find(params[:id])
  end

  def validation_params
    params.require(:validation).permit(:name)
  end
end
