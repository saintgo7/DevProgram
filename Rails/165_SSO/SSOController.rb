class SSOController < ApplicationController
  before_action :set_sso, only: [:show, :edit, :update, :destroy]

  # GET /sso
  def index
    @ssos = SSO.all
    render json: @ssos
  end

  # GET /sso/1
  def show
    render json: @sso
  end

  # POST /sso
  def create
    @sso = SSO.new(sso_params)

    if @sso.save
      render json: @sso, status: :created
    else
      render json: @sso.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sso/1
  def update
    if @sso.update(sso_params)
      render json: @sso
    else
      render json: @sso.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sso/1
  def destroy
    @sso.destroy
    head :no_content
  end

  private

  def set_sso
    @sso = SSO.find(params[:id])
  end

  def sso_params
    params.require(:sso).permit(:name)
  end
end
