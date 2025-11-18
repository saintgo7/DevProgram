class SettingsController < ApplicationController
  before_action :set_settings, only: [:show, :edit, :update, :destroy]

  # GET /settings
  def index
    @settingss = Settings.all
    render json: @settingss
  end

  # GET /settings/1
  def show
    render json: @settings
  end

  # POST /settings
  def create
    @settings = Settings.new(settings_params)

    if @settings.save
      render json: @settings, status: :created
    else
      render json: @settings.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /settings/1
  def update
    if @settings.update(settings_params)
      render json: @settings
    else
      render json: @settings.errors, status: :unprocessable_entity
    end
  end

  # DELETE /settings/1
  def destroy
    @settings.destroy
    head :no_content
  end

  private

  def set_settings
    @settings = Settings.find(params[:id])
  end

  def settings_params
    params.require(:settings).permit(:name)
  end
end
