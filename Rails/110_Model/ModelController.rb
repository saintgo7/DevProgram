class ModelController < ApplicationController
  before_action :set_model, only: [:show, :edit, :update, :destroy]

  # GET /model
  def index
    @models = Model.all
    render json: @models
  end

  # GET /model/1
  def show
    render json: @model
  end

  # POST /model
  def create
    @model = Model.new(model_params)

    if @model.save
      render json: @model, status: :created
    else
      render json: @model.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /model/1
  def update
    if @model.update(model_params)
      render json: @model
    else
      render json: @model.errors, status: :unprocessable_entity
    end
  end

  # DELETE /model/1
  def destroy
    @model.destroy
    head :no_content
  end

  private

  def set_model
    @model = Model.find(params[:id])
  end

  def model_params
    params.require(:model).permit(:name)
  end
end
