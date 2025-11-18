class PreferenceController < ApplicationController
  before_action :set_preference, only: [:show, :edit, :update, :destroy]

  # GET /preference
  def index
    @preferences = Preference.all
    render json: @preferences
  end

  # GET /preference/1
  def show
    render json: @preference
  end

  # POST /preference
  def create
    @preference = Preference.new(preference_params)

    if @preference.save
      render json: @preference, status: :created
    else
      render json: @preference.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /preference/1
  def update
    if @preference.update(preference_params)
      render json: @preference
    else
      render json: @preference.errors, status: :unprocessable_entity
    end
  end

  # DELETE /preference/1
  def destroy
    @preference.destroy
    head :no_content
  end

  private

  def set_preference
    @preference = Preference.find(params[:id])
  end

  def preference_params
    params.require(:preference).permit(:name)
  end
end
