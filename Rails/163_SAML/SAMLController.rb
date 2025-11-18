class SAMLController < ApplicationController
  before_action :set_saml, only: [:show, :edit, :update, :destroy]

  # GET /saml
  def index
    @samls = SAML.all
    render json: @samls
  end

  # GET /saml/1
  def show
    render json: @saml
  end

  # POST /saml
  def create
    @saml = SAML.new(saml_params)

    if @saml.save
      render json: @saml, status: :created
    else
      render json: @saml.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /saml/1
  def update
    if @saml.update(saml_params)
      render json: @saml
    else
      render json: @saml.errors, status: :unprocessable_entity
    end
  end

  # DELETE /saml/1
  def destroy
    @saml.destroy
    head :no_content
  end

  private

  def set_saml
    @saml = SAML.find(params[:id])
  end

  def saml_params
    params.require(:saml).permit(:name)
  end
end
