class AssetController < ApplicationController
  before_action :set_asset, only: [:show, :edit, :update, :destroy]

  # GET /asset
  def index
    @assets = Asset.all
    render json: @assets
  end

  # GET /asset/1
  def show
    render json: @asset
  end

  # POST /asset
  def create
    @asset = Asset.new(asset_params)

    if @asset.save
      render json: @asset, status: :created
    else
      render json: @asset.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /asset/1
  def update
    if @asset.update(asset_params)
      render json: @asset
    else
      render json: @asset.errors, status: :unprocessable_entity
    end
  end

  # DELETE /asset/1
  def destroy
    @asset.destroy
    head :no_content
  end

  private

  def set_asset
    @asset = Asset.find(params[:id])
  end

  def asset_params
    params.require(:asset).permit(:name)
  end
end
