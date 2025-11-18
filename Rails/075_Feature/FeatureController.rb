class FeatureController < ApplicationController
  before_action :set_feature, only: [:show, :edit, :update, :destroy]

  # GET /feature
  def index
    @features = Feature.all
    render json: @features
  end

  # GET /feature/1
  def show
    render json: @feature
  end

  # POST /feature
  def create
    @feature = Feature.new(feature_params)

    if @feature.save
      render json: @feature, status: :created
    else
      render json: @feature.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /feature/1
  def update
    if @feature.update(feature_params)
      render json: @feature
    else
      render json: @feature.errors, status: :unprocessable_entity
    end
  end

  # DELETE /feature/1
  def destroy
    @feature.destroy
    head :no_content
  end

  private

  def set_feature
    @feature = Feature.find(params[:id])
  end

  def feature_params
    params.require(:feature).permit(:name)
  end
end
